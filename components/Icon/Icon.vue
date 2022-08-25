<template>
  <div :style="{ height: size, width: size }">
    <component
        :is="defineAsyncComponent(IconRegistry[props.name])"
        :class="{ spinning: isSpinning }"
        :is-solid="isSolid"
        :style="{ height: size, width: size, fill: color }"
    />
  </div>
</template>

<script lang="ts" setup>
import { IconRegistry } from "@/components/Icon/IconRegistry";
import { defineAsyncComponent } from "vue";

const props = defineProps({
  name: {
    type: String,
    required: true
  },
  size: {
    type: String,
    default: "1rem"
  },
  color: {
    type: String,
    default: "inherit"
  },
  isSolid: {
    type: Boolean,
    default: false
  },
  isSpinning: {
    type: Boolean,
    default: false
  }
});
</script>