<template>
  <div id="home">
    <div class="home__column">
      <MainHeroPanel />

      <SocialsPanel />

      <BecomeADeveloperPanel />

      <PowersPanel />

      <LocationPanel />
    </div>

    <div class="home__column">
      <WhyCodePanel />

      <SubscribePanel />

      <WhyUsPanel />

      <UpLeveledPanel />
    </div>
  </div>
</template>

<script lang="ts" setup>
import { useHead } from "#head";
import BecomeADeveloperPanel from "~/pages/home/features/BecomeADeveloperPanel.vue";
import LocationPanel from "~/pages/home/features/LocationPanel.vue";
import MainHeroPanel from "~/pages/home/features/MainHeroPanel.vue";
import PowersPanel from "~/pages/home/features/PowersPanel.vue";
import SocialsPanel from "~/pages/home/features/SocialsPanel.vue";
import SubscribePanel from "~/pages/home/features/SubscribePanel.vue";
import UpLeveledPanel from "~/pages/home/features/UpLeveledPanel.vue";
import WhyCodePanel from "~/pages/home/features/WhyCodePanel.vue";
import WhyUsPanel from "~/pages/home/features/WhyUsPanel.vue";

useHead({
  title: "Home - The Earth Is Square // Think Outside The Square"
});
</script>

<style lang="scss" scoped>
#home {
  display: grid;
  flex: 1;
  grid-template-columns: 2fr 1fr;
  grid-gap: 0.6rem;

  .home__column {
    display: grid;
    margin-bottom: auto;
    grid-template-columns: repeat(12, 1fr);
    grid-gap: 0.6rem;
    grid-auto-rows: 5vh;
  }
}
</style>