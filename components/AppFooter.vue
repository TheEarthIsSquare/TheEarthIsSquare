<template>
  <footer>
    <div class="footer__content">
      <div class="footer__logo">
        <h1>THE EARTH<br />IS SQUARE</h1>
        <span>© {{ (new Date).getFullYear() }} The Earth Is Square Ltd. </span>
      </div>

      <div class="footer__address">
        Revolver Lane <br />
        231 Chapel Street <br />
        Prahran, 3181 <br />
        Melbourne, VIC, Australia
      </div>

      <div class="footer__links">
        <router-link to="contact">Contact</router-link>
        <router-link to="imprint">Imprint</router-link>
        <router-link to="privacy">Privacy Policy</router-link>
        <router-link to="toc">Terms and Conditions</router-link>
      </div>

      <div class="footer__socials">
        <SocialIcon name="instagram" size="3.2rem" />
        <SocialIcon name="twitter" size="3.2rem" />
        <SocialIcon name="youtube" size="3.2rem" />
        <SocialIcon name="discord" size="3.2rem" />
        <SocialIcon name="linkedIn" size="3.2rem" />
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
    font-size: 1.2rem;
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
        font-size: 42.55px;
        line-height: 72.19%;
        transform: rotate(-2.6deg);
        text-align: center;
        color: var(--white);
      }

      span {
        font-weight: bold;
      }
    }

    .footer__address {
      font-weight: bold;
    }

    .footer__links {
      font-weight: bold;
      display: flex;
      flex-direction: column;

      a {
        transition: all 0.25s ease;
        text-decoration: underline;

        &:hover {
          color: var(--pink);
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