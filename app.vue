<template>
  <div id="app">
    <TheSidebar :isOpen="isSidebarOpen" @toggle-sidebar="isSidebarOpen = !isSidebarOpen" />
    <div id="main" :class="{ '--sidebar-open': isSidebarOpen }">
      <NuxtPage />
    </div>
  </div>
</template>

<script lang="ts" setup>
import { ref } from "@vue/reactivity";

const isSidebarOpen = ref(false);
</script>

<style lang="scss">
#app {
  display: flex;
  width: 100vw;
  height: 100vh;

  #main {
    display: flex;
    flex: 1;
    margin-left: 75px;
    transition: margin-left 0.25s ease;
    background: linear-gradient(247.29deg, #EB2188 7.21%, #D909DD 91.17%);

    &.--sidebar-open {
      margin-left: 375px;
    }
  }
}
</style>