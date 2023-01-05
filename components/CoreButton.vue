<template>
  <button
      :class="[`--${variant}`, size === 'L' && '--large']"
      :style="{ width, height, boxShadow: ` 0.8rem 0.8rem 0 var(--Color-${backgroundColor})` }"
      @submit="emit('submit')"
  >
    <slot />
  </button>
</template>

<script lang="ts" setup>
import { PropType } from "@vue/runtime-core";

defineProps({
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
    type: String as PropType<"Black" | "White">,
    default: "Black"
  }
});

const emit = defineEmits(["submit"]);
</script>

<style lang="scss" scoped>
button {
  font-size: var(--FontSize-M);
  font-weight: var(--FontWeight-Bold);
  transition: all 0.25s ease;
  border: none;
  border-radius: var(--BorderRadius-L);

  &.--primary {
    color: var(--Color-White);
    background: var(--Gradient-PinkPurple);
  }

  &.--secondary {
    padding: 1rem 1.5rem;
    border: 3px solid var(--Color-Black);
    background-color: var(--Color-White);

    &:hover {
      color: var(--Color-White);
      border: 3px solid var(--Color-White);
      background-color: var(--Color-Black);
    }
  }

  &.--large {
    font-size: var(--FontSize-L);
    padding: 2rem;
  }
}
</style>