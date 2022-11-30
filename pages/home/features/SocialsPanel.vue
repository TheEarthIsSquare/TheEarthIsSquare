<template>
  <div class="socials">
    <SocialIcon name="instagram" />
    <SocialIcon name="twitter" />
    <SocialIcon name="youtube" />
    <SocialIcon name="discord" />
    <SocialIcon name="linkedIn" />
  </div>
</template>

<style lang="scss" scoped>
.socials {
  display: flex;
  align-items: center;
  flex-direction: column;
  justify-content: space-evenly;
  padding: 2rem 0;
  color: var(--white);
  grid-column: span 1;
  grid-row: span 5;
}
</style>