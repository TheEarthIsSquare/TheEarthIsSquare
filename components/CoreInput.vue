<template>
  <div class="input-wrapper" @click="focusInput()">
    <label>{{ label }}{{ isRequired ? "*" : "" }}</label>
    <input ref="inputRef" :required="isRequired" :type="type" @change="evt => emit('onChange', evt.target.value)"/>
  </div>
</template>

<script lang="ts" setup>
defineProps({
  label: {
    type: String,
    required: true
  },
  type: {
    type: String,
    default: "text"
  },
  isRequired: {
    type: Boolean,
    default: false
  }
})

const emit = defineEmits(['onChange']);

const inputRef = ref<HTMLInputElement | null>(null);
const focusInput = () => {
  if (inputRef.value) {
    inputRef.value.focus();
  }
}
</script>

<style lang="scss" scoped>
@import 'assets/style/variables.scss';


.input-wrapper {
  flex: 1;
  display: flex;
  flex-direction: column;
  box-shadow: var(--Shadow-Border), var(--Shadow-L);
  border: none;
  border-radius: var(--BorderRadius-L);
  padding: 1rem 2rem;
  cursor: text;

  label {
    font-size: var(--FontSize-S);
    font-weight: var(--FontWeight-Bold);
    cursor: text;
  }

  input {
    border: none;
    box-shadow: none;
  }
}
</style>