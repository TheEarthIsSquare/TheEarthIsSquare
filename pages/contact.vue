<template>
  <div id="contact">
    <div class="contact__blurb">
      <h2>Contact Us</h2>
      <p>Contact us for a quote, a coffee, or to get drunk and vent about your parents.</p>
    </div>
    <div class="contact__mediums">
      <div class="contact__mediums-item">
        <div class="contact-mediums-item-icon">
          <Icon name="map" size="100px" />
        </div>
        Revolver Lane, 231 Chapel St, Prahran VIC 3181
      </div>

      <div class="contact__mediums-item">
        <div class="contact-mediums-item-icon">
          <Icon name="phone" size="100px" />
        </div>
        +61 467 444 975
      </div>

      <div class="contact__mediums-item">
        <div class="contact-mediums-item-icon">
          <Icon name="envelope" size="100px" />
        </div>
        hello@theearthissquare.com
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { definePageMeta } from "#imports";

definePageMeta({
  title: "The Earth Is Square - Contact Us"
});
</script>

<style lang="scss" scoped>
#contact {
  display: flex;
  align-items: center;
  flex: 1;
  flex-direction: column;
  justify-content: center;

  .contact__blurb {
    text-align: center;
    color: white;

    h2 {
      font-size: 68px;
      margin-bottom: 0;
    }

    p {
      font-size: 24px;
      width: 550px;
      margin-top: 0;
      opacity: 0.75;
    }
  }

  .contact__mediums {
    display: grid;
    margin-top: 80px;
    grid-template-columns: repeat(3, 1fr);
    grid-gap: 40px;

    .contact__mediums-item {
      font-size: 20px;
      display: grid;
      align-items: center;
      justify-content: center;
      width: 300px;
      text-align: center;
      color: white;
      grid-template-rows: 200px auto;

      .contact-mediums-item-icon {
        display: flex;
        align-items: center;
        justify-content: center;
        fill: white;
      }
    }
  }
}
</style>