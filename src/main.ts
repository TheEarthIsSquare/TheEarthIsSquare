import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
// @ts-ignore
import VueKinesis from "vue-kinesis";
import VueGtag from "vue-gtag-next";

createApp(App)
  .use(router)
  .use(VueKinesis)
  .use(VueGtag, {
    property: {
      id: "G-XEXHEZY5TL"
    }
  })
  .mount("#app");
