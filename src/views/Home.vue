<template>
  <div class="home">
    <section class="main container">
      Test
    </section>
  </div>
</template>

<script>
export default {
  name: 'Home'
}
</script>

<style scoped lang="scss">
@import '../styles/variables';

.home {
  padding-top: 100px;
  background-color: $martinique;
  color: white;

  section.main {
    height: 100vh;
  }
}
</style>
