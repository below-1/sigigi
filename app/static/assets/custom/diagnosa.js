$(document).ready(function () {
    var app = new Vue({
        el: "#app",
        data: {
            listGejala: [ ],
            error: false,
            loading: false,
            activeIndex: 0
        },
        computed: {
            activeGejala () {
                var activeIndex = this.activeIndex
                var listGejala = this.listGejala
                if (activeIndex == listGejala.length - 1) {
                    return undefined
                }
                return listGejala[activeIndex]
            },
            progress () {
                if (this.listGejala.length == 0) return 0
                return (this.activeIndex) / ((this.listGejala.length - 1) * 1.0) * 100
            },
            selectedGejala () {
                return this.listGejala.filter(gejala => gejala.selected)
            }
        },
        mounted () {
            this.loadGejala()
        },
        methods: {
            loadGejala () {
              this.loading = true
              fetch('/api/vcirs/gejala')
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

            },
            reset () {
                this.activeIndex = 0
                this.listGejala.forEach(gejala => {
                    gejala.selected = false
                })
            },
            next (val) {
                var activeIndex = this.activeIndex
                var listGejala = this.listGejala
                if (activeIndex == listGejala.length) return
                listGejala[activeIndex].selected = val
                if (activeIndex == listGejala.length - 1) return
                this.activeIndex += 1
            }
        }
    })
})