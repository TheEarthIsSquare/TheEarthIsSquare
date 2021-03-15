import { createApp } from "vue";
import App from "./App.vue";
import store from "./store";
import router from "./router";
// @ts-ignore
import VueKinesis from "vue-kinesis";
import VueGtag from "vue-gtag-next";

createApp(App)
  .use(router)
  .use(store)
  .use(VueKinesis)
  .use(VueGtag, {
    useDebugger: true,
    property: {
      id: "G-XEXHEZY5TL"
    }
  })
  .mount("#app");
