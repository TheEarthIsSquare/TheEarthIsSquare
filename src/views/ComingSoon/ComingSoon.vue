<template>
  <KinesisContainer id="ComingSoon" duration="2000">
    <KinesisElement class="content">
      <h4 class="name">think outside the square</h4>
      <h1>THE EARTH<br>IS SQUARE</h1>
      <h3 class="blurb">new website, coming soon.</h3>
      <div class="divider"/>
      <h3 class="contact">hello@theearthissquare.com</h3>
      <div class="socials">
        <a href="https://twitter.com/_EarthIsSquare" target="_blank">
          <img alt="Twitter" src="../../assets/icons/twitter-brands.svg"/>
        </a>
        <a href="https://discord.com/invite/X23epKN" target="_blank">
          <img alt="Discord" src="../../assets/icons/discord-brands.svg"/>
        </a>
        <a href="https://www.youtube.com/channel/UC_FBMBKup_b3xk_NfeKlalQ" target="_blank">
          <img alt="YouTube" src="../../assets/icons/youtube-brands.svg"/>
        </a>
      </div>
    </KinesisElement>
    <div class="logo">
      <KinesisElement><div class="square --topLeftSquare"/></KinesisElement>
      <KinesisElement><div class="square --topRightSquare"/></KinesisElement>
      <KinesisElement strength="20"><div class="square --bottomLeftSquare"/></KinesisElement>
      <KinesisElement><div class="square --bottomRightSquare"/></KinesisElement>
    </div>
  </KinesisContainer>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'ComingSoon',
  setup() {
    return
  }
})
</script>

<style lang="scss" scoped>
#ComingSoon {
  height: 100vh;
  display: grid;
  grid-gap: 100px;
  grid-template-columns: 1fr 1fr;
  align-items: center;

  .content {
    justify-self: flex-end;
    text-align: right;

    .name {
      font-weight: 900;
      opacity: 0.6;
      margin: 0;
      color: #ff0081;
    }

    .blurb {
      margin: 0;
      opacity: 0.8;
    }

    h1 {
      margin: 0;
      font-weight: 900;
      font-size: 64px;
      line-height: 1;
    }

    .divider {
      opacity: 0.4;
      background-color: #2d3436;
      height: 1px;
      width: 100%;
      margin: 20px 0;
    }

    .contact {
      font-weight: bold;
      margin: 0;
      opacity: 0.8;
    }

    .socials {
      margin-top: 10px;
      display: flex;
      flex-direction: row-reverse;

      a {
        opacity: 0.8;
        transition: 0.25s ease;
        width: 30px;
        margin-left: 10px;

        &:hover {
          opacity: 1;
        }
      }
    }
  }

  .logo {
    width: 200px;
    height: 200px;
    display: grid;
    grid-template: 1fr 1fr / 1fr 1fr;

    .square {
      background-color: #2d3436;
      height: 100px;
      width: 100px;

      &.--bottomLeftSquare {
        transform: translate3d(-25px, 25px, 0);
      }
    }
  }
}
</style>
