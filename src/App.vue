<template>
  <div id="app">
    <nav class="navigation-wrapper">
      <div class="navigation container">
        <router-link :to="{ name: 'Home' }">
          <div class="navigation__logo">
            the earth <span>is square</span>
            <div class="navigation__logo-square"/>
          </div>
        </router-link>
        <div class="menu-toggle" @click="toggleMenu">
          menu
        </div>
      </div>
    </nav>
    <div class="navigation-menu" v-if="openMenu">

    </div>
    <router-view/>
  </div>
</template>

<script lang="ts">
import { Vue } from 'vue-property-decorator';

export default class App extends Vue {
  openMenu: boolean = false

  toggleMenu(): void {
    this.openMenu = !this.openMenu
  }
}
</script>

<style lang="scss">
@import './styles/variables';
@import './styles/_base';

#app {
  font-family: 'Open Sans', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;

  .navigation-wrapper {
    width: 100%;
    height: 100px;
    position: absolute;
    color: white;

    .navigation {
      display: flex;
      justify-content: space-between;
      align-items: center;
      height: 100%;

      .navigation__logo {
        display: flex;
        font-weight: bold;
        font-size: 24px;
        color: white;

        span {
          padding-left: 5px;
          color: $rose;
        }

        .navigation__logo-square {
          background-color: $rose;
          height: 5px;
          width: 5px;
          margin: 0 0 7px 5px;
          align-self: flex-end;
        }
      }

      .menu-toggle {
        margin-left: auto;
        font-weight: bold;
        cursor: pointer;
      }
    }
  }

  .navigation-menu {
    position: fixed;
    background-color: $rose;
    width: 100vw;
    height: 100vh;
  }
}
</style>
