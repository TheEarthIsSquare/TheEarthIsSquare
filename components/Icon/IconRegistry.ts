export type IconName = keyof typeof IconRegistry;

export const IconRegistry = {

    // BoxIcons - https://boxicons.com
    leftArrowAlt: () => import(/* webpackPrefetch: true */ "./IconComponents/IconLeftArrowAlt.vue"),
    rightArrowAlt: () => import(/* webpackPrefetch: true */ "./IconComponents/IconRightArrowAlt.vue"),
    map: () => import(/* webpackPrefetch: true */ "./IconComponents/IconMap.vue"),
    phone: () => import(/* webpackPrefetch: true */ "./IconComponents/IconPhone.vue"),
    envelope: () => import(/* webpackPrefetch: true */ "./IconComponents/IconEnvelope.vue"),
    rocket: () => import(/* webpackPrefetch: true */ "./IconComponents/IconRocket.vue"),
    graduation: () => import(/* webpackPrefetch: true */ "./IconComponents/IconGraduation.vue"),
    notepad: () => import(/* webpackPrefetch: true */ "./IconComponents/IconNotepad.vue"),
    networkChart: () => import(/* webpackPrefetch: true */ "./IconComponents/IconNetworkChart.vue"),
    laptop: () => import(/* webpackPrefetch: true */ "./IconComponents/IconLaptop.vue"),
    hot: () => import(/* webpackPrefetch: true */ "./IconComponents/IconHot.vue"),
    chevronDown: () => import(/* webpackPrefetch: true */ "./IconComponents/IconChevronDown.vue"),
    loaderAlt: () => import(/* webpackPrefetch: true */ "./IconComponents/IconLoaderAlt.vue"),

    discord: () => import(/* webpackPrefetch: true */ "./IconComponents/IconDiscord.vue"),
    instagram: () => import(/* webpackPrefetch: true */ "./IconComponents/IconInstagram.vue"),
    youtube: () => import(/* webpackPrefetch: true */ "./IconComponents/IconYoutube.vue"),
    twitter: () => import(/* webpackPrefetch: true */ "./IconComponents/IconTwitter.vue"),
    linkedIn: () => import(/* webpackPrefetch: true */ "./IconComponents/IconLinkedIn.vue"),
    facebook: () => import(/* webpackPrefetch: true */ "./IconComponents/IconFacebookSquare.vue"),

    // Custom Icons
    teis: () => import(/* webpackPrefetch: true */ "./IconComponents/IconTEIS.vue"),
};