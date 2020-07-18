<template>
  <div class="logo" :class="{ dark : dark }">
    the earth <span>is square</span>
    <div class="logo-square"/>
  </div>
</template>

<script>
export default {
  name: "TheLogo",
  props: {
    dark: {
      type: Boolean,
      default: false
    }
  }
}
</script>

<style lang="scss" scoped>
@import '../styles/variables';

.logo {
  display: flex;
  font-weight: bold;
  font-size: 24px;
  color: white;

  span {
    transition: color 0.25s ease;
    padding-left: 5px;
    color: $rose;
  }

  .logo-square {
    transition: background-color 0.25s ease;
    background-color: $rose;
    height: 5px;
    width: 5px;
    margin: 0 0 7px 5px;
    align-self: flex-end;
  }

  &.dark {
    span {
      color: $martinique;
    }

    .logo-square {
      background-color: $martinique;
    }
  }
}
</style>