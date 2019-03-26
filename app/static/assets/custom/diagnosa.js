$(document).ready(function () {
    var app = new Vue({
        el: "#app",
        data: {
            listGejala: [ ],
            error: false,
            loading: false
        },
        mounted () {
            this.loadGejala()
        },
        methods: {
            loadGejala () {
              this.loading = true
              fetch('/api/gejala')
                .then(resp => resp.json())
                .then(items => {
                  this.listGejala = items.map(it => {
                    return Object.assign({ selected: false, ...it })
                  })
                })
                .catch(err => {
                    console.log(err)
                    this.error = true
                })
                .then(() => {
                    this.loading = false
                })
            },
            diagnosa () {
                var selectedGejala = this.listGejala.filter(gejala => gejala.selected)
                var payload = {
                    gejala: selectedGejala
                }
                const url = `/admin/users/diagnosa/${VUE_USER_ID}`
                fetch(url, {
                    method: 'POST',
                    body: JSON.stringify(payload),
                    headers: {
                        'Content-Type': 'application/json'
                    }
                })
                    .then(resp => resp.json())
                    .then(data => {
                        console.log(data)
                    })
                    .catch(err => {
                        console.log(err)
                    })
                    .then(() => {
                        window.location = `/admin/users/detail/${VUE_USER_ID}`
                    })

            }
        }
    })
})