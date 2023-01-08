// https://v3.nuxtjs.org/api/configuration/nuxt.config
export default defineNuxtConfig({
    modules: [
        '@funken-studio/sitemap-nuxt-3'
    ],
    css: [
        "@/assets/style/main.scss"
    ],
    // @ts-ignore
    sitemap: {
        hostname: 'https://theearthissquare.com',
        gzip: true,
        filter: ({ routes }: { routes: any }) => {
            return routes.filter((route: any) => !route.name.includes('features')).map((route: any) => {
                if (route.name === 'home') {
                    route.url = '/';
                }

                return route;
            });
        },
    }
});