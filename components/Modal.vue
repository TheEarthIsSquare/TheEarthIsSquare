<template>
  <slot :toggleOpen="() => isOpen = !isOpen" name="trigger"/>

  <Teleport to="body">
    <div :class="{ '--open': isOpen }" class="modal__wrapper">
      <div class="modal">
        <slot name="content"/>
      </div>

      <div class="modal__backdrop" @click="isOpen = false"/>
    </div>
  </Teleport>
</template>

<script lang="ts" setup>
const isOpen = ref(false);
</script>

<style lang="scss" scoped>
.modal__wrapper {
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  display: none;
  align-items: center;
  justify-content: center;
  z-index: 100;

  &.--open {
    display: flex;
  }

  .modal__backdrop {
    position: absolute;
    top: 0;
    right: 0;
    bottom: 0;
    left: 0;
    background-color: rgba(0, 0, 0, 0.4);
  }

  .modal {
    height: 80rem;
    width: 40vw;
    background-color: var(--Color-White);
    border-radius: var(--BorderRadius-L);
    box-shadow: var(--Shadow-Border) var(--Shadow-L);
    display: flex;
    z-index: 200;
  }
}
</style>