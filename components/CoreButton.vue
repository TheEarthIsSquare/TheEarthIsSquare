<template>
  <button
      :class="[`--${variant}`, size === 'L' && '--large']"
      :style="{ width, height, boxShadow: ` 0.8rem 0.8rem 0 var(--${backgroundColor})` }"
      @submit="emit('submit')"
  >
    <slot />
  </button>
</template>

<script lang="ts" setup>
import { PropType } from "@vue/runtime-core";

const props = defineProps({
  variant: {
    type: String as PropType<"primary" | "secondary">,
    default: "primary"
  },
  size: {
    type: String as PropType<"L" | "S">,
    default: "S"
  },
  width: {
    type: String,
    default: "auto"
  },
  height: {
    type: String,
    default: "auto"
  },
  backgroundColor: {
    type: String as PropType<"black" | "white">,
    default: "black"
  }
});

const emit = defineEmits(["submit"]);
</script>

<style lang="scss" scoped>
button {
  font-size: 17.28px;
  font-weight: bold;
  transition: all 0.25s ease;
  border: none;
  border-radius: 3rem;

  &.--primary {
    color: var(--white);
    background: linear-gradient(247.29deg, #EB2188 7.21%, #D909DD 91.17%);
  }

  &.--secondary {
    padding: 1rem 1.5rem;
    border: 3px solid var(--black);
    background-color: var(--white);

    &:hover {
      color: var(--white);
      border: 3px solid var(--white);
      background-color: var(--black);
    }
  }

  &.--large {
    font-size: 24.88px;
    padding: 2rem;
  }
}
</style>