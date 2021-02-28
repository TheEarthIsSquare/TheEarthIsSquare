import { createApp } from "vue";
import App from "./App.vue";
import store from "./store";
import router from "./router";
// @ts-ignore
import VueKinesis from "vue-kinesis";

createApp(App).use(router).use(store).use(VueKinesis).mount("#app");
