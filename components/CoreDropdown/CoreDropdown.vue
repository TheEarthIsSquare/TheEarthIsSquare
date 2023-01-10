<template>
  <VDropdown :placement="placement" :shown="isOpen">
    <button class="dropdown__button" type="button" @click="isOpen = !isOpen">
      <div v-if="selectedOption?.leftImage || selectedOption?.leftIcon" class="dropdown__button-icon">
        <img v-if="selectedOption?.leftImage" :alt="selectedOption?.label" :src="selectedOption?.leftImage"/>
        <Icon v-else :name="selectedOption?.leftIcon" size="1.6rem"/>
      </div>

      <div class="dropdown__button-text">
        <div class="dropdown__title">
          {{ title }}
        </div>
        <div class="dropdown__selected-label">
          {{ selectedOption ? selectedOption?.label : "Select an option..." }}
        </div>
      </div>

      <div class="dropdown__button-chevron">
        <Icon name="chevronDown" size="1.4rem"/>
      </div>
    </button>

    <template #popper>
      <div class="dropdown__menu">
        <div v-for="option in options" :key="option.value" class="dropdown__menu-option" @click="selectOption(option)">
          {{ option.label }}
        </div>
      </div>
    </template>
  </VDropdown>
</template>

<script lang="ts" setup>
import Icon from "~/components/Icon/Icon.vue";
import type { DropdownOption } from "@/components/CoreDropdown/CoreDropdown.types";
import type { PropType } from "vue";
import { ref } from "vue";

const props = defineProps({
  options: {
    type: Array as PropType<DropdownOption[]>,
    required: true
  },
  initialSelectedValue: {
    type: String,
    required: false
  },
  placement: {
    type: String,
    default: 'auto'
  },
  title: {
    type: String,
    required: true
  }
})
const emit = defineEmits(['onSelect'])
const isOpen = ref(false);
const selectedOption = ref<DropdownOption | null>(props.initialSelectedValue ? props.options.find(o => o.value == props.initialSelectedValue) || null : null);
const selectOption = (option: DropdownOption) => {
  emit('onSelect', option.value);
  selectedOption.value = option;
  isOpen.value = false;
}
</script>

<style lang="scss" scoped>
.dropdown__button {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 0.4rem;
  background-color: var(--Color-White);
  border-radius: var(--BorderRadius-L);
  color: var(--Color-Black);
  height: 100%;
  padding: 1rem 2rem;
  border: none;
  cursor: pointer;
  box-shadow: var(--Shadow-L), var(--Shadow-Border);
  width: 100%;

  .dropdown__button-icon {
    display: flex;
    align-items: center;
    justify-content: center;
    background-color: var(--Color-Black);
    border-radius: 0.3rem;
    padding: 0.4rem;
    height: 2.2rem;
    width: 2.2rem;
    fill: var(--Color-Black);

    img {
      height: 100%;
      width: auto;
    }
  }

  .dropdown__button-text {
    display: flex;
    flex-direction: column;
    text-align: left;

    .dropdown__title {
      font-size: var(--FontSize-S);
      font-weight: var(--FontWeight-Bold);
      cursor: pointer;
    }

    .dropdown__selected-label {
      padding: 0.1rem 0.2rem;
    }
  }

  .dropdown__button-chevron {
    display: flex;
    align-items: center;
    justify-content: center;
    fill: var(--Color-Black);
    padding-left: 1rem;
  }
}

.dropdown__menu {
  display: flex;
  flex-direction: column;
  border-radius: var(--BorderRadius-L);
  padding: 1rem;

  .dropdown__menu-option {
    padding: 0.5rem 1rem;
    border-radius: var(--BorderRadius-L);
    cursor: pointer;
    transition: all 0.25s ease;
    font-size: var(--FontSize-S);

    &:hover {
      background-color: var(--Color-Black);
      color: var(--Color-White);
    }
  }
}
</style>