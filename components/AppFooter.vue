<template>
  <footer>
    <div class="footer__content">
      <div class="footer__logo">
        <h1>THE EARTH<br/>IS SQUARE</h1>
        <span>© {{ (new Date).getFullYear() }} The Earth Is Square Ltd. </span>
      </div>

      <div class="footer__address">
        Revolver Lane <br/>
        231 Chapel Street <br/>
        Prahran, 3181 <br/>
        Melbourne, VIC, Australia
      </div>

      <div class="footer__links">
        <NuxtLink to="mailto:office@theearthissquare.com">Contact</NuxtLink>
        <NuxtLink to="imprint">Imprint</NuxtLink>
        <NuxtLink to="privacy">Privacy Policy</NuxtLink>
        <NuxtLink to="toc">Terms and Conditions</NuxtLink>
      </div>

      <div class="footer__socials">
        <SocialIcon name="instagram" size="3.2rem"/>
        <SocialIcon name="twitter" size="3.2rem"/>
        <SocialIcon name="youtube" size="3.2rem"/>
        <SocialIcon name="discord" size="3.2rem"/>
        <SocialIcon name="linkedIn" size="3.2rem"/>
      </div>
    </div>
  </footer>
</template>

<script lang="ts" setup>

</script>

<style lang="scss" scoped>
footer {
  display: flex;
  margin-top: auto;
  color: white;

  .footer__content {
    font-size: var(--FontSize-S);
    display: flex;
    align-items: center;
    flex: 1;
    justify-content: space-evenly;
    height: 15rem;

    .footer__logo {
      display: flex;
      align-items: center;
      flex-direction: column;
      gap: 1rem;

      h1 {
        font-size: var(--FontSize-Chonky-S);
        line-height: 72.19%;
        transform: rotate(-2.6deg);
        text-align: center;
        color: var(--Color-White);
      }

      span {
        font-weight: var(--FontWeight-Bold);
      }
    }

    .footer__address {
      font-weight: var(--FontWeight-Bold);
    }

    .footer__links {
      font-weight: var(--FontWeight-Bold);
      display: flex;
      flex-direction: column;

      a {
        transition: all 0.25s ease;
        text-decoration: underline;

        &:hover {
          color: var(--Color-Pink);
        }
      }
    }

    .footer__socials {
      display: flex;
      gap: 1rem;
    }
  }
}
</style>