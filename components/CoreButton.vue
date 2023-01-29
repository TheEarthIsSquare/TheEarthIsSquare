<template>
  <button
      :class="[`--${variant}`, size === 'L' && '--large', {'--loading': isLoading}]"
      :style="{ ...customStyle }"
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
  iconLeft: {
    type: String as PropType<IconName>,
    required: false
  },
  isLoading: {
    type: Boolean,
    default: false
  },
  customStyle: {
    type: Object,
    default: {}
  }
});

const emit = defineEmits(["submit"]);
</script>

<style lang="scss" scoped>
@import 'assets/style/variables.scss';

button {
  position: relative;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  font-size: var(--FontSize-M);
  font-weight: var(--FontWeight-Bold);
  transition: all 0.25s ease;
  border-radius: var(--BorderRadius-L);
  padding: 1rem 1.5rem;
  border: 0.3rem solid var(--Color-Black);
  box-shadow: var(--Shadow-S);
  z-index: 1;

  @media screen and (max-width: $BreakPoint-Tablet) {
    font-size: var(--FontSize-XS);
    border-radius: var(--BorderRadius-M);
  }

  &.--large {
    font-size: var(--FontSize-L);
    box-shadow: var(--Shadow-M);
    padding: 2rem;

    @media screen and (max-width: $BreakPoint-Tablet) {
      font-size: var(--FontSize-S);
      padding: 1rem 1.5rem;
    }
  }

  &.--loading {
    pointer-events: none;
  }

  &.--primary {
    color: var(--Color-White);
    background: var(--Gradient-PinkPurple);

    &::before {
      position: absolute;
      content: "";
      top: 0;
      right: 0;
      bottom: 0;
      left: 0;
      background: var(--Gradient-PinkPurple-Darker);
      z-index: -1;
      transition: opacity 0.25s linear;
      opacity: 0;
      border-radius: var(--BorderRadius-L);
    }

    &:hover {
      &::before {
        opacity: 1;
      }
    }
  }

  &.--secondary {
    background-color: var(--Color-White);

    &:hover {
      background-color: var(--Color-Light-Grey);
    }
  }
}
</style>