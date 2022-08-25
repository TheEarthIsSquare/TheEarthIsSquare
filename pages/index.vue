<template>
  <div id="home">
    <h1>
      The Earth<br>
      Is Square
    </h1>
  </div>
</template>

<script lang="ts" setup>
import { definePageMeta } from "#imports";

definePageMeta({
  title: "The Earth Is Square - Development & Creativity - Think Outside The Square"
});
</script>

<style lang="scss" scoped>
#home {
  display: flex;
  align-items: center;
  flex: 1;
  justify-content: center;

  h1 {
    font-size: 222px;
    line-height: 72%;
    transform: rotate(-5deg);
    transform-origin: left top;
    text-transform: uppercase;
    color: white;
  }
}
</style>