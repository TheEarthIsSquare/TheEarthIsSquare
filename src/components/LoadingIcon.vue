<template>
  <div class="loading-icon" :class="{ transparent: transparent }">
    <square color="#FF0081"/>
    <div class="loading-icon__message" v-if="showMessage">
      <span>{{ message }}...</span>
    </div>
  </div>
</template>

<script>
export default {
  name: 'LoadingIcon',
  props: {
    percentage: {
      type: Number,
      default: 0
    },
    showMessage: {
      type: Boolean,
      default: true
    },
    message: {
      type: String,
      default: 'Loading'
    },
    transparent: {
      type: Boolean,
      default: false
    }
  }
}
</script>

<style scoped lang="scss">
.loading-icon {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;

  &.transparent {
    background-color: transparent;
  }

  .loading-icon__message {
    font-weight: bold;
  }
}
</style>