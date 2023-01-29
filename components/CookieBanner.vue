<template>
  <div v-if="!cookiePermission" class="cookie-banner-wrapper">
    <div class="cookie-banner">
      <div class="cookie-banner__blurb">
        We use third-party cookies in order to personalize your site experience.
      </div>

      <div class="cookie-banner__actions">
        <CoreButton @click="accept">
          Allow
        </CoreButton>
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { config } from 'vue-gtag';

const cookiePermission = useCookie('cookiePermission', { maxAge: 1704085200 });

const accept = () => {
  config({ enabled: true });
  cookiePermission.value = "true";
}
</script>

<style lang="scss" scoped>
.cookie-banner-wrapper {
  display: flex;
  justify-content: center;
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  z-index: 1000;
  padding: 1rem;

  .cookie-banner {
    font-size: var(--FontSize-S);
    padding: 2rem 4rem;
    background-color: var(--Color-White);
    border-radius: var(--BorderRadius-L);
    border: 0.3rem solid var(--Color-Black);
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 6rem;

    .cookie-banner__actions {
      display: flex;
      align-items: center;
      gap: 2rem;
    }
  }
}
</style>