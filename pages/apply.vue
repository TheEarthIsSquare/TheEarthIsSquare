<template>
  <div id="apply">
    <h1>APPLICATIONS<br/>OPEN SOON</h1>
    <h2>Connect with us</h2>
    <div class="apply__socials">
      <SocialIcon name="instagram" size="5.2rem"/>
      <SocialIcon name="twitter" size="5.2rem"/>
      <SocialIcon name="youtube" size="5.2rem"/>
      <SocialIcon name="discord" size="5.2rem"/>
      <SocialIcon name="linkedIn" size="5.2rem"/>
    </div>
  </div>
</template>

<style lang="scss" scoped>
#apply {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: white;
  border-radius: var(--BorderRadius-L);
  flex-direction: column;

  h1 {
    text-align: center;
    font-size: var(--FontSize-Chonky-Chonk);
    line-height: 72.19%;
    color: var(--Color-White);
    text-shadow: var(--Shadow-Border), var(--Shadow-L);
  }

  h2 {
    margin-top: 5rem;
    font-size: var(--FontSize-XL);
    text-shadow: var(--Shadow-Border);
    color: var(--Color-White);
  }

  .apply__socials {
    margin-top: 1rem;
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 1rem;
  }
}
</style>