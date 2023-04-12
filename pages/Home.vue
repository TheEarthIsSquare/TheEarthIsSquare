<template>
  <div id="home">
    <template v-if="isDesktop">
      <div class="home__column">
        <MainHeroPanel/>

        <SocialsPanel/>

        <BecomeADeveloperPanel/>

        <PowersPanel/>

        <UpLeveledPanel/>
      </div>

      <div class="home__column">
        <WhyCodePanel/>

        <SubscribePanel/>

        <WhyUsPanel/>
      </div>
    </template>

    <template v-else>
      <div class="home__column">
        <MainHeroPanel/>

        <SubscribePanel/>

        <WhyCodePanel/>

        <WhyUsPanel/>

        <UpLeveledPanel/>
      </div>
    </template>
  </div>
</template>

<script lang="ts" setup>
import BecomeADeveloperPanel from "~/features/home/BecomeADeveloperPanel.vue";
import MainHeroPanel from "~/features/home/MainHeroPanel.vue";
import PowersPanel from "~/features/home/PowersPanel.vue";
import SocialsPanel from "~/features/home/SocialsPanel.vue";
import SubscribePanel from "~/features/home/SubscribePanel.vue";
import UpLeveledPanel from "~/features/home/UpLeveledPanel.vue";
import WhyCodePanel from "~/features/home/WhyCodePanel.vue";
import WhyUsPanel from "~/features/home/WhyUsPanel.vue";
import { useScreen } from "~/hooks/useScreen";

useSeoMeta({
  title: "Learn To Code in Melbourne - Web Development Bootcamp",
  description:
    `Looking to jumpstart your career in web development? Our Melbourne-based bootcamp offers comprehensive
    training in the latest programming languages and web technologies. With hands-on projects and experienced instructors,
    you'll gain the skills and confidence needed to succeed in this exciting field. Enroll now and join the ranks of
    successful web developers in Melbourne and beyond.`
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