import VueGtag from 'vue-gtag'

export default defineNuxtPlugin((nuxtApp) => {
    nuxtApp.vueApp.use(VueGtag, {
        config: {
            id: 'G-HYCL30MX7K',
            enabled: false,
        }
    }, nuxtApp.$router)
})