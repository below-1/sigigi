from app.config import DEBUG
import json

def vucr(rules, list_gejala_id):

    non_counter = {}
    vucr = []

    set_gejala = set()

    for rule in rules:
        for slot in rule.slots:
            gejala_id = slot.gejala_id
            set_gejala.add(gejala_id)

    # Initialize non_counter
    for gejala_id in set_gejala:
        non_counter[gejala_id] = 0

    # print('non_counter=', non_counter)

    for rule in rules:

        slots = [ slot.as_dict() for slot in rule.slots ]
        penyakit = rule.penyakit

        rule_data = {
            'penyakit': penyakit.id,
            'slots': slots
        }

        n = len(slots)
        gejala_rows = []
        total = 0
        for slot in slots:
            gejala_id = slot['gejala_id']
            vorder = slot['vorder']
            non_counter[gejala_id] += 1
            vur = 1 * non_counter[gejala_id] * vorder / (n * 1.0)
            slot['vur'] = vur
            total += vur

        rule_data['nurj'] = total / n * 1.0
        rule_data['rur'] = rule_data['nurj'] / n
        rule_data['total_VUR'] = sum([slot['vur'] for slot in slots])

        total_NUR_norm = rule_data['total_VUR'] * 1.0
        # print(rule_data)
        for slot in slots:
            slot['vur_norm'] = slot['vur'] / total_NUR_norm

        vucr.append(rule_data)

    # Bayes step
    for rule_data in vucr:
        slots = rule_data['slots']
        t1 = [ slot['weight'] for slot in slots ]
        total_t1 = sum(t1)
        t2 = [ _t1 / total_t1 for _t1 in t1 ]
        t3 = [ _t1 * _t2 for (_t1, _t2) in zip(t1, t2) ]
        total_t3 = sum(t3)
        t4 = [ (_t1 * _t2) / total_t3 for (_t1, _t2) in zip(t1, t2) ]
        t5 = [ _t1 * _t4 for (_t1, _t4) in zip(t1, t4) ]
        believe = sum(t5)
        rule_data['believe'] = believe

    for rule_data in vucr:
        slots = rule_data['slots']

        for slot in slots:
            # slot['credit'] = 1 + slot['weight']
            slot['credit'] = 1

        total_credit = sum([ slot['credit'] for slot in slots ])

        for slot in slots:
            slot['credit_norm'] = slot['credit'] / total_credit * 1.0
        #
        # total_credit_norm = sum([slot['credit_norm'] for slot in slots])
        #
        # for slot in slots:
        #     slot['vur_baru'] = slot['vur'] / total_credit * 1.0
        #
        # total_vur_baru = sum([ slot['vur_baru'] for slot in slots ])
        #
        # for slot in slots:
        #     slot['vur_baru_norm'] = slot['vur_baru'] / total_vur_baru * 1.0

    for rule_data in vucr:
        total_vur = 0
        total_vur_norm = 0
        for slot in slots:
            total_vur += slot['vur']
            total_vur_norm += slot['vur_norm']

        rule_data['total_vur'] = total_vur
        rule_data['total_vur_norm'] = total_vur_norm

    for gejala_id in list_gejala_id:
        for rule_data in vucr:
            for slot in rule_data['slots']:
                if (slot['gejala_id'] != gejala_id):  continue
                slot['credit'] += slot['weight']

    penyakit_id = None
    max_nur = -1
    for rule_data in vucr:
        slots = rule_data['slots']
        total_credit = sum([slot['credit'] for slot in slots])

        for slot in slots:
            slot['credit_norm'] = slot['credit'] / total_credit * 1.0

        for slot in slots:
            vur_credit = slot['credit_norm'] * non_counter[slot['gejala_id']] * (slot['vorder'] / len(slots))
            slot['vur'] = vur_credit

        total_vur = sum([slot['vur'] for slot in slots])
        for slot in slots:
            slot['vur_norm'] = slot['vur'] * 1.0 / total_vur


        total_vur_norm = sum([slot['vur_norm'] for slot in slots])
        rule_data['total_vur'] = total_vur
        rule_data['total_vur_norm'] = total_vur_norm
        rule_data['nur'] = total_vur_norm * 1.0 / len(rule_data['slots'])
        if (rule_data['nur'] > max_nur):
            penyakit_id = rule_data['penyakit']
            #
            # for slot in slots:
            #     slot['vur_baru'] = slot['vur'] / total_credit * 1.0
            #
            # total_vur_baru = sum([ slot['vur_baru'] for slot in slots ])
            #
            # for slot in slots:
            #     slot['vur_baru_norm'] = slot['vur_baru'] / total_vur_baru * 1.0


    # for rule_data in vucr:
    #     total_vur_baru = 0
    #     total_vur_baru_norm = 0
    #     total_credit = 0
    #     total_credit_norm = 0
    #     total_vur = 0
    #     for slot in slots:
    #         total_vur += slot['vur']
    #         total_vur_baru += slot['vur_baru']
    #         total_credit += slot['credit']
    #         total_credit_norm += slot['credit_norm']
    #         total_vur_baru_norm += slot['vur_baru_norm']
    #
    #     rule_data['total_vur'] = total_vur
    #     rule_data['total_vur_baru'] = total_vur_baru
    #     rule_data['total_vur_baru_norm'] = total_vur_baru_norm
    #     rule_data['total_credit'] = total_credit
    #     rule_data['total_credit_norm'] = total_credit_norm

    if DEBUG: print(json.dumps(vucr, indent=4))

    result = {
        'vucr': vucr,
        'penyakit_id': penyakit_id
    }


    return result
