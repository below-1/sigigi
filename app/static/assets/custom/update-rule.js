$(document).ready(function () {
    var app = new Vue({
        el: "#main-card",
        data: {
            hello: 'World',
            listPenyakit: [],
            listGejala: [],
            selectedPenyakitId: null
        },
        mounted () {
            if (!VUE_ID_RULE) {
                alert("Terjadi kesalahan. ID Rule tidak ditemukan")
                throw new Error("ID RULE IS UNDEFINED")
            }
            this.loadData(VUE_ID_RULE)
            alert('HERE')
            console.log(VUE_ID_RULE)
        },
        methods: {

            loadData (id) {
                return fetch(`/api/rules/${id}`)
                    .then(resp => resp.json())
                    .then(data => {
                        console.log(data)
                        this.listPenyakit = data.list_penyakit
                        this.listGejala = data.list_gejala
                        this.selectedPenyakitId = data.penyakit_id

                        console.log('selected=', this.listGejala.map(it => it.selected))
                    })
                    .catch(err => {
                        console.log(err)
                        alert('Terjadi kesalahan saat load data!')
                    })
            },

            saveRule () {
                var penyakit_id = this.selectedPenyakitId
                var gejala = this.listGejala.filter(g => g.selected)
                var payload = {
                    id: VUE_ID_RULE,
                    penyakit_id,
                    gejala
                }
                payload = JSON.stringify(payload)
                var options = {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: payload
                }
                var url = `/admin/rules/update/${VUE_ID_RULE}`

                fetch(url, options)
                    .then(() => {
                        window.location = "/admin/rules"
                    })
                    .catch(err => {
                        console.log(err)
                        alert("Terjadi kesalahan")
                        window.location.reload()
                    })
            }
        }
    })
})