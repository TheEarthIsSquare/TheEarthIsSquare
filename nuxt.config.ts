import { defineNuxtConfig } from "nuxt";

// https://v3.nuxtjs.org/api/configuration/nuxt.config
export default defineNuxtConfig({
  app: {
    head: {
      charset: "utf-16",
      title: "The Earth Is Square",
      meta: [
        // { name: "description", content: "My amazing site." }
      ],
    }
  },
  css: [
    "@/assets/style/main.scss"
  ],
});
