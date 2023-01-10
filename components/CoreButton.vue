<template>
  <button
      :class="[`--${variant}`, size === 'L' && '--large', {'--loading': isLoading}]"
      :style="{ width, height, boxShadow: ` 0.8rem 0.8rem 0 var(--Color-${backgroundColor})` }"
      @submit="emit('submit')"
  >
    <div v-if="iconLeft || isLoading" class="icon-left">
      <Icon
          :isSpinning="isLoading" :name="isLoading ? 'loaderAlt' : iconLeft"
          :size="size === 'L' ? '2.344rem' : '1.875rem'"
      />
    </div>

    <slot/>
  </button>
</template>

<script lang="ts" setup>
import { PropType } from "@vue/runtime-core";
import { IconName } from "~/components/Icon/IconRegistry";
import Icon from "~/components/Icon/Icon.vue";

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
  },
  iconLeft: {
    type: String as PropType<IconName>,
    required: false
  },
  isLoading: {
    type: Boolean,
    default: false
  }
});

const emit = defineEmits(["submit"]);
</script>

<style lang="scss" scoped>
button {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  font-size: var(--FontSize-M);
  font-weight: var(--FontWeight-Bold);
  transition: all 0.25s ease;
  border: none;
  border-radius: var(--BorderRadius-L);

  &.--loading {
    pointer-events: none;
  }

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
    height: 4.8rem;
    font-size: var(--FontSize-L);
    padding: 2rem;
  }
}
</style>