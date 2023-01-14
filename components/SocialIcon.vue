<template>
  <a :href="getLink()" target="_blank">
    <Icon :name="name" :size="size"/>
  </a>
</template>

<script lang="ts" setup>
import { PropType } from "@vue/runtime-core";

const props = defineProps({
  name: {
    type: String as PropType<"instagram" | "twitter" | "youtube" | "linkedIn" | "discord">,
    required: true
  },
  size: {
    type: String,
    default: "5rem"
  }
});

const getLink = () => {
  switch (props.name) {
    case "instagram":
      return "https://instagram.com/theearthissquare.au";
    case "twitter":
      return "https://twitter.com/EarthIsSquareAU";
    case "youtube":
      return "https://www.youtube.com/@TheEarthIsSquare";
    case "linkedIn":
      return "https://www.linkedin.com/company/the-earth-is-square";
    case "discord":
      return "https://discord.com/invite/X23epKN";
  }
};
</script>

<style lang="scss" scoped>
a {
  transition: all 0.25s ease;

  &:hover {
    color: var(--Color-Pink);
    fill: var(--Color-Pink);
  }
}
</style>