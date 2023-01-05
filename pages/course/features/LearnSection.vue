<template>
  <section id="learn">
    <div class="learn__inner-wrapper">
      <h2>
        Ready to start your next chapter?<br />
        <span>Here’s what you’ll learn.</span>
      </h2>

      <div class="learn__tabs">
        <div v-for="(tab, index) in tabs"
             :class="{ '--selected': selectedTabIndex === index }"
             class="learn__tab"
             @click="selectedTabIndex = index"
        >
          {{ tab.label }}
        </div>
      </div>

      <div class="learn__content">
        <div class="learn__content-text">
          {{ selectedTab.content }}
        </div>
        <div :style="{ backgroundImage: `url('${selectedTab.image}')`}" class="learn__content-hero" />
      </div>
    </div>
  </section>
</template>

<script lang="ts" setup>
import { computed, ref } from "#imports";
import bestPracticesImage from "@/assets/img/best-practices.png";
import technologiesImage from "@/assets/img/technologies.png";
import toolsImage from "@/assets/img/tools.png";

const tabs = [
  {
    label: "Tools",
    image: toolsImage,
    content: `
    With the popular developer tools you will encounter in the real world. That’s why we will use tools like the
    command line, GitHub, VS Code and may more right from the start.
    `
  },
  {
    label: "Technologies",
    image: technologiesImage,
    content: `
    Our state-of-the-art curriculum guides you through JavaScript, HTML, CSS, Node.js, React and all the computer
    science fundamentals you need to become an expert developer.
    `
  },
  {
    label: "Best Practices",
    image: bestPracticesImage,
    content: `
    In programming, you are never alone and always learning. You will be part of a community, experience team work
    using current workflows and learn how to keep up to date with the latest technologies.
    `
  }
];

const selectedTabIndex = ref(0);
const selectedTab = computed(() => tabs[selectedTabIndex.value]);
</script>

<style lang="scss" scoped>
#learn {
  display: flex;
  align-content: center;
  justify-content: center;
  padding: 10rem;
  color: var(--Color-White);

  .learn__inner-wrapper {
    font-weight: var(--FontWeight-Bold);
    display: flex;
    align-content: center;
    flex-direction: column;
    justify-content: center;
    max-width: var(--View-MaxWidth);
    gap: 5rem;

    h2 {
      font-size: var(--FontSize-Chonky-M);
      text-align: center;

      span {
        background: var(--Gradient-PinkPurple);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: none;
      }
    }

    .learn__tabs {
      font-size: var(--FontSize-XXL);
      display: flex;
      align-content: center;
      justify-content: space-around;

      .learn__tab {
        padding: 1rem 2rem;
        cursor: pointer;
        transition: all 0.25s ease;
        opacity: 0.6;
        border-bottom: 0.3rem solid transparent;

        &.--selected {
          opacity: 1;
          border-bottom: 0.3rem solid var(--Color-White);
        }
      }
    }

    .learn__content {
      font-size: var(--FontSize-L);
      display: grid;
      align-items: center;
      padding: 10rem 0;
      grid-template-columns: 2fr 3fr;
      grid-gap: 10rem;

      .learn__content-hero {
        width: 100%;
        height: 30vh;
        border: 0.3rem solid var(--Color-Black);
        border-radius: var(--BorderRadius-L);
        background-position-y: center;
        background-size: cover;
        box-shadow: var(--Shadow-L);
      }
    }
  }
}
</style>