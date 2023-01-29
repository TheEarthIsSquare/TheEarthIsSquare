<template>
  <div id="home">
    <template v-if="isDesktop">
      <div class="home__column">
        <MainHeroPanel/>

        <SocialsPanel/>

        <BecomeADeveloperPanel/>

        <PowersPanel/>

        <LocationPanel/>
      </div>

      <div class="home__column">
        <WhyCodePanel/>

        <SubscribePanel/>

        <WhyUsPanel/>

        <UpLeveledPanel/>
      </div>
    </template>

    <template v-else>
      <div class="home__column">
        <MainHeroPanel/>

        <SubscribePanel/>

        <WhyCodePanel/>

        <WhyUsPanel/>

        <UpLeveledPanel/>
        
        <LocationPanel/>
      </div>
    </template>
  </div>
</template>

<script lang="ts" setup>
import { useHead } from "#head";
import BecomeADeveloperPanel from "~/features/home/BecomeADeveloperPanel.vue";
import LocationPanel from "~/features/home/LocationPanel.vue";
import MainHeroPanel from "~/features/home/MainHeroPanel.vue";
import PowersPanel from "~/features/home/PowersPanel.vue";
import SocialsPanel from "~/features/home/SocialsPanel.vue";
import SubscribePanel from "~/features/home/SubscribePanel.vue";
import UpLeveledPanel from "~/features/home/UpLeveledPanel.vue";
import WhyCodePanel from "~/features/home/WhyCodePanel.vue";
import WhyUsPanel from "~/features/home/WhyUsPanel.vue";
import { useScreen } from "~/hooks/useScreen";

useHead({
  title: "Learn To Code in Melbourne - The Earth Is Square"
});

const { isDesktop } = useScreen();
</script>

<style lang="scss" scoped>
@import 'assets/style/variables.scss';

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

  @media screen and (max-width: $BreakPoint-Tablet) {
    grid-template-columns: 1fr;
  }
}
</style>