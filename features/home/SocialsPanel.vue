<template>
  <div class="socials">
    <SocialIcon name="instagram"/>
    <SocialIcon name="twitter"/>
    <SocialIcon name="youtube"/>
    <SocialIcon name="linkedIn"/>
    <SocialIcon name="facebook"/>
  </div>
</template>

<style lang="scss" scoped>
@import 'assets/style/variables.scss';

.socials {
  display: flex;
  align-items: center;
  flex-direction: column;
  justify-content: space-evenly;
  padding: 2rem 0;
  color: var(--Color-White);
  grid-column: span 1;
  grid-row: span 5;
}
</style>