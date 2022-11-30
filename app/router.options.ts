import type { RouterConfig } from "@nuxt/schema";

// https://router.vuejs.org/api/interfaces/routeroptions.html
export default <RouterConfig>{
  routes: (_routes) => [
    { name: "home", path: "/", component: () => import("~/pages/home/index.vue") },
    { name: "course", path: "/course", component: () => import("~/pages/course/index.vue") },
    { name: "apply", path: "/apply", component: () => import("~/pages/apply.vue") },
    { name: "contact", path: "/contact", component: () => import("~/pages/contact.vue") },
    { name: "imprint", path: "/imprint", component: () => import("~/pages/imprint.vue") },
    { name: "info", path: "/info", component: () => import("~/pages/info.vue") },
    { name: "privacy", path: "/privacy", component: () => import("~/pages/privacy.vue") },
    { name: "toc", path: "/toc", component: () => import("~/pages/toc.vue") }
  ]
};
