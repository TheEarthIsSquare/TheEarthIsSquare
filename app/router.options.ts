import type { RouterConfig } from "@nuxt/schema";
import Home from "~/pages/home/index.vue";
import Course from "~/pages/course/index.vue";
import Apply from "~/pages/apply.vue";
import Contact from "~/pages/contact.vue";
import Imprint from "~/pages/imprint.vue";
import Info from "~/pages/info.vue";
import Privacy from "~/pages/privacy.vue";
import TOC from "~/pages/toc.vue";

export default <RouterConfig>{
  routes: (_routes) => [
    { name: "home", path: "/", component: Home },
    { name: "course", path: "/course", component: Course },
    { name: "apply", path: "/apply", component: Apply },
    { name: "contact", path: "/contact", component: Contact },
    { name: "imprint", path: "/imprint", component: Imprint },
    { name: "info", path: "/info", component: Info },
    { name: "privacy", path: "/privacy", component: Privacy },
    { name: "toc", path: "/toc", component: TOC },
  ]
};
