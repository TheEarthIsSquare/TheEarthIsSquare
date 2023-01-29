export const useScreen = () => {
    const width = ref(process.client ? window.innerWidth : 0);
    const height = ref(process.client ? window.innerHeight : 0);

    if (process.client) {
        window.addEventListener('resize', () => {
            width.value = window.innerWidth
        })

        window.addEventListener('resize', () => {
            height.value = window.innerHeight
        })
    }

    return {
        width, height,
        isMobile: computed(() => width.value <= 600),
        isTablet: computed(() => width.value > 600 && width.value < 1280),
        isDesktop: computed(() => width.value >= 1280)
    }
}