import numpy as np
import pandas as pd

bayes_rules = {
  'Karies Gigi': {
    'G1': 0.6,
    'G2': 0.4,
    'G3': 0.2,
    'G4': 0.9,
    'G5': 0.1,
    'G6': 0.5,
    'G7': 0.8,
    'G8': 0.2
  },
  'Gingivitis': {
    'G5': 0.1,
    'G9': 0.2,
    'G10': 0.4,
    'G11': 0.1,
    'G12': 0.7,
    'G13': 0.5,
    'G14': 0.5,
    'G15': 0.6

  },
  'Periodontitis':{
    'G5': 0.1,
    'G9': 0.2,
    'G11': 0.1,
    'G12': 0.7,
    'G13': 0.5,
    'G14': 0.5,
    'G15': 0.6,
    'G16': 0.3,
    'G17': 0.1
  },
  'Abses':{
    'G1': 0.6,
    'G5': 0.1,
    'G11': 0.1,
    'G12': 0.7,
    'G13': 0.5,
    'G14': 0.5,
    'G15': 0.6,
    'G18': 0.8,
    'G19': 0.7
  },
  'Pulpitis':{
    'G2': 0.4,
    'G4': 0.9,
    'G6': 0.5,
    'G12': 0.7,
    'G19': 0.7,
    'G20': 0.4,
    'G21': 0.9
  },
  'Erosi Gigi':{
    'G2': 0.4,
    'G7': 0.8,
    'G22': 0.6,
    'G23': 0.8
  }
}

df = pd.DataFrame({
  'Karies Gigi': [
    0.6,
    0.4,
    0.2,
    0.9,
    0.1,
    0.5,
    0.8,
    0.2,
    np.NAN,
    np.NAN,
    np.NAN,
    np.NAN,
    np.NAN,
    np.NAN,
    np.NAN,
    np.NAN,
    np.NAN,
    np.NAN,
    np.NAN,
    np.NAN,
    np.NAN,
    np.NAN,
    np.NAN
  ],
  'Gingivitis': [
    np.NAN,
    np.NAN,
    np.NAN,
    np.NAN,
    0.1,
    np.NAN,
    np.NAN,
    np.NAN,
    0.2,
    0.4,
    0.1,
    0.7,
    0.5,
    0.5,
    0.6,
    np.NAN,
    np.NAN,
    np.NAN,
    np.NAN,
    np.NAN,
    np.NAN,
    np.NAN,
    np.NAN
  ],
  'Periodontitis': [
    np.NAN,
    np.NAN,
    np.NAN,
    np.NAN,
    0.1,
    np.NAN,
    np.NAN,
    np.NAN,
    0.2,
    np.NAN,
    0.1,
    0.7,
    0.5,
    0.5,
    0.6,
    0.3,
    0.1,
    np.NAN,
    np.NAN,
    np.NAN,
    np.NAN,
    np.NAN,
    np.NAN
  ],
  'Abses': [
    0.6,
    np.NAN,
    np.NAN,
    np.NAN,
    0.1,
    np.NAN,
    np.NAN,
    np.NAN,
    np.NAN,
    np.NAN,
    0.1,
    0.7,
    0.5,
    0.5,
    0.6,
    np.NAN,
    np.NAN,
    0.8,
    0.7,
    np.NAN,
    np.NAN,
    np.NAN,
    np.NAN
  ],
  'Pulpitis': [
    np.NAN,
    0.4,
    np.NAN,
    0.9,
    np.NAN,
    0.5,
    np.NAN,
    np.NAN,
    np.NAN,
    np.NAN,
    np.NAN,
    0.7,
    np.NAN,
    np.NAN,
    np.NAN,
    np.NAN,
    np.NAN,
    np.NAN,
    0.7,
    0.4,
    0.9,
    np.NAN,
    np.NAN
  ],
  'Erosi Gigi': [
    np.NAN,
    0.4,
    np.NAN,
    np.NAN,
    np.NAN,
    np.NAN,
    0.8,
    np.NAN,
    np.NAN,
    np.NAN,
    np.NAN,
    np.NAN,
    np.NAN,
    np.NAN,
    np.NAN,
    np.NAN,
    np.NAN,
    np.NAN,
    np.NAN,
    np.NAN,
    np.NAN,
    0.6,
    0.8
  ]
})

df.index = [
  'Demam',
  'Sakit Gigi',
  'Demam Terlihat',
  'Gigi Berlubang',
  'Bau Mulut Tak Sedap',
  'Infeksi Jaringan Pulpa',
  'Gigi ngilu saat terkena ransangan (panas atau dingin)',
  'Gigi berwarna, hitam, atau putih pada permukaan gigi',
  'Gusi nyeri',
  'Gusi gatal',
  'Gusi bengkak',
  'Gusi mudah berdarah',
  'Gusi merah terang',
  'Terdapat endapan plak',
  'Terdapat karang gigi',
  'Gigi goyang',
  'Rongga terbentuk di antara gigi (Nanah terbentuk)',
  'Nanah pada pangkal gusi',
  'Nyeri saat menguyah',
  'Lubang sangat besar pada gigi',
  'Ruang pulpa terbuka',
  'Gigi tampak lebih kuning',
  'Tepi gigi menjadi tidak terakhir'
]


rules = [
  {
    'penyakit': 'Karies Gigi',
    'gejalas': [
      (1, 'G1'),
      (2, 'G2'),
      (3, 'G3'),
      (4, 'G4'),
      (5, 'G5'),
      (6, 'G6'),
      (7, 'G7'),
      (8, 'G8')
    ]
  },
  {
    'penyakit': 'Gingivitis',
    'gejalas': [
      (1, 'G9'),
      (2, 'G10'),
      (3, 'G11'),
      (4, 'G12'),
      (5, 'G5'),
      (6, 'G13'),
      (7, 'G14'),
      (8, 'G15')
    ]
  },
  {
    'penyakit': 'Periodontitis',
    'gejalas': [
      (1, 'G5'),
      (2, 'G16'),
      (3, 'G11'),
      (4, 'G9'),
      (5, 'G13'),
      (6, 'G12'),
      (7, 'G14'),
      (8, 'G15'),
      (9, 'G17')
    ]
  },
  {
    'penyakit': 'Abses',
    'gejalas': [
      (1, 'G1'),
      (2, 'G5'),
      (3, 'G11'),
      (4, 'G13'),
      (5, 'G12'),
      (6, 'G18'),
      (7, 'G19'),
      (8, 'G14'),
      (9, 'G15')
    ]
  },
  {
    'penyakit': 'Pulpitis',
    'gejalas': [
      (1, 'G2'),
      (2, 'G4'),
      (3, 'G6'),
      (4, 'G12'),
      (5, 'G19'),
      (6, 'G20'),
      (7, 'G21')
    ]
  },
  {
    'penyakit': 'Erosi Gigi',
    'gejalas': [
      (1, 'G2'),
      (2, 'G22'),
      (3, 'G7'),
      (4, 'G23')
    ]
  }
]

non_counter = {

}
# Initialize
for i in range(1, 24):
    non_counter['G{}'.format(i)] = 0

def debug(cond, *val):
    if cond:
        print(*val)

vucr = []
for i in range(len(rules)):
    data = rules[i]
    gejalas = data['gejalas']
    n = len(gejalas)
    gejalas_rows = []
    total = 0
    for vorder, name in gejalas:
        non_counter[name] += 1
        vur = 1 * non_counter[name] * vorder / (n * 1.0)
        gejalas_rows.append({
          'vorder': vorder,
          'name': name,
          'vur': vur
        })
        total += vur
    data['nurj'] = total / n * 1.0
    # debug(cond, '')
    # debug(cond, 'NURJ: ', data['nurj'])
    # debug(cond, [ g['vur'] for g in gejalas_rows ])
    data['grows'] = gejalas_rows
    data['total_VUR'] = sum([ g['vur'] for g in gejalas_rows ])

    total_NUR_norm = data['total_VUR'] * 1.0
    for g in gejalas_rows:
        g['vur_norm'] = g['vur'] / total_NUR_norm

    data['NUR'] = 1.0 / n
    data['vur_norm'] = sum([ g['vur'] / total_NUR_norm for g in gejalas_rows ])

    vucr.append(data)
    # print(data)
    # input()

for i in range(len(rules)):
    pass

# print(rules)
NON = [ (index, df.loc[index].notnull().sum()) for index in df.index ]
print(non_counter)

bayes_result = []
for curr_key, seqs in bayes_rules.items():
    current = bayes_rules[curr_key]
    key_seq = list(current.keys())
    t1 = list(current.values())
    total = sum(t1)
    t2 = [ t / total for t in t1 ]
    t3 = [ _t1 * _t2 for (_t1, _t2) in zip(t1, t2) ]
    total_t3 = sum(t3)
    t4 = [ (_t1 * _t2) / total_t3 for (_t1, _t2) in zip(t1, t2) ]
    t5 = [ _t1 * _t4 for (_t1, _t4) in zip(t1, t4) ]
    tingkat_keper = sum(t5)
    bayes_result.append({
      't1': t1,
      't2': t2,
      't3': t3,
      't4': t4,
      't5': t5,
      'believe': tingkat_keper
    })

# curr_key = 'Karies Gigi'
# current = bayes_rules[curr_key]
# print(list(current.keys()))

# print(vucr)
# print(bayes_result)
for v in vucr:
    key = v['penyakit']
    old_vurs = [ x['vur'] for x in v['grows'] ]
    gejalas = [ g for _, g in v['gejalas'] ]
    old_vurs = { g: v for g, v in zip(gejalas, old_vurs) }

    v['credit'] = {}
    for _, g in v['gejalas']:
        v['credit'][g] = 1 + bayes_rules[key][g]
    total_credit = sum(v['credit'].values())
    v['norm_credit'] = { g: v['credit'][g] for _, g in v['gejalas']  }
    v['total_credit'] = total_credit
    v['VUR_baru'] = { g: old_vurs[g] / total_credit for g in gejalas }
    total_vur_baru = sum(v['VUR_baru'].values())
    v['VUR_baru_norm'] = { g: old_v / total_vur_baru for g, old_v in v['VUR_baru'].items() }

    print(v)
    input()