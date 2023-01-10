<template>
  <div class="checkbox-wrapper">
    <div v-if="title" class="checkbox-wrapper__title" @click="clickInput">{{ title }}</div>
    <div class="checkbox-main">
      <label @click="clickInput">{{ label }}</label>
      <input ref="inputRef" v-model="checkboxValue" type="checkbox" @change="onChange"/>
    </div>
  </div>
</template>

<script lang="ts" setup>
const props = defineProps({
  label: {
    type: String,
    required: true
  },
  title: {
    type: String,
    required: false
  },
  isChecked: {
    type: Boolean,
    default: false
  }
})

const emit = defineEmits(['onChange'])

const checkboxValue = ref(props.isChecked);

const inputRef = ref<HTMLInputElement | null>(null);
const clickInput = () => {
  if (inputRef.value) {
    inputRef.value.click();
  }
}

const onChange = () => {
  emit('onChange', checkboxValue.value)
}
</script>

<style lang="scss" scoped>
.checkbox-wrapper {
  display: flex;
  flex-direction: column;
  align-items: flex-end;

  .checkbox-wrapper__title {
    font-weight: var(--FontWeight-Bold);
    font-size: var(--FontSize-S);
    cursor: pointer;
  }

  .checkbox-main {
    display: flex;
    gap: 1rem;
    cursor: pointer;
    font-weight: var(--FontWeight-Bold);
    align-items: center;

    label {
      cursor: pointer;
    }

    input {

    }
  }
}
</style>