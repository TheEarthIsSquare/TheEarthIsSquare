<template>
  <div id="app">
    <NavBar />

    <main>
      <NuxtPage />
      <AppFooter />
    </main>
  </div>
</template>

<script lang="ts" setup>
import { useHead } from "#head";

useHead({
  title: "The Earth Is Square"
});
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