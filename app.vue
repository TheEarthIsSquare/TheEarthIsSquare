<template>
  <div id="app">
    <NavBar/>

    <main>
      <NuxtPage/>
      <AppFooter/>

      <CookieBanner/>
    </main>
  </div>
</template>

<script lang="ts" setup>
import { useHead } from "#head";
import CookieBanner from "~/components/CookieBanner.vue";
import { config } from "vue-gtag";

useHead({
  title: "The Earth Is Square",
  link: [
    {
      rel: "preconnect",
      href: 'https://fonts.gstatic.com',
      crossorigin: "anonymous"
    },
    {
      rel: "preload",
      href: "https://fonts.googleapis.com/css2?family=Raleway:wght@400;700;900&family=Passion+One:wght@900&display=swap",
      as: "style"
    }
  ]
});

const cookiePermission = useCookie('cookiePermission');

onMounted(() => {
  if (Boolean(cookiePermission.value)) {
    config({ enabled: true });
  }
})
</script>

<style lang="scss">
#app {
  position: relative;
  display: flex;
  overflow: hidden;
  flex-direction: column;
  height: 100vh;
  padding: 0.6rem;
  background: var(--Color-Black);
  gap: 0.6rem;

  main {
    display: flex;
    overflow-y: scroll;
    flex-direction: column;
    height: calc(100vh - 11.2rem);
    margin-top: 11.2rem;
  }
}
</style>