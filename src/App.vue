<template>
  <div id="app">
    <nav class="navigation-wrapper" :class="{ open : isMenuOpen }">
      <div class="navigation container">
        <div class="logo-wrapper" @click="closeMenu">
          <router-link :to="{ name: 'Home' }">
            <Logo :dark="isMenuOpen"/>
          </router-link>
        </div>
        <div class="menu-toggle__wrapper" @click="toggleMenu">
          <transition name="fade" mode="out-in">
            <div class="menu-toggle" :key="'menu'" v-if="!isMenuOpen">
              <div class="menu-toggle__text">menu</div>
              <font-awesome-icon icon="bars"/>
            </div>
            <div class="menu-toggle" :key="'close'" v-else>
              <div class="menu-toggle__text">close</div>
              <font-awesome-icon icon="times"/>
            </div>
          </transition>
        </div>
      </div>
    </nav>
    <NavigationMenu :open="isMenuOpen" @close="closeMenu"/>
    <div class="view-wrapper">
      <transition name="fade" mode="out-in">
        <router-view :class="{ 'menu-open' : isMenuOpen }"/>
      </transition>
    </div>
    <footer class="container">
      <Logo/>
      <div class="footer-socials">
        <a href="https://www.instagram.com/_earthissquare">
          <font-awesome-icon :icon="['fab', 'instagram']" size="2x"/>
        </a>
      </div>
      <div class="footer-copyright">
        &copy; 2020 The Earth is Square. All rights reserved.
      </div>
    </footer>
  </div>
</template>

<script>
import Logo from './components/TheLogo'
import NavigationMenu from "./components/NavigationMenu/NavigationMenu"

export default {
  name: 'Home',
  components: { Logo, NavigationMenu },
  data() {
    return {
      isMenuOpen: false
    }
  },
  computed: {
    currentRoute() {
      return this.$route.name
    }
  },
  watch: {
    currentRoute(previousRoute, currentRoute) {
      if (previousRoute !== currentRoute){
        this.isMenuOpen = false
      }
    }
  },
  methods: {
    closeMenu() {
      this.isMenuOpen = false
    },
    toggleMenu() {
      this.isMenuOpen = !this.isMenuOpen
    }
  }
}
</script>

<style lang="scss">
@import './styles/variables';
@import './styles/_base';
@import './styles/animations';
@import url('https://fonts.googleapis.com/css2?family=Open+Sans:ital,wght@0,300;0,400;0,600;0,700;0,800;1,300;1,400;1,600;1,700;1,800&display=swap');

#app {
  font-family: 'Open Sans', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;

  .navigation-wrapper {
    z-index: 2000;
    width: 100%;
    height: 100px;
    position: absolute;
    color: white;

    &.open {
      position: fixed;
    }

    .navigation {
      display: flex;
      justify-content: space-between;
      align-items: center;
      height: 100%;

      .menu-toggle__wrapper {
        margin-left: auto;
        font-weight: bold;
        cursor: pointer;

        .menu-toggle {
          display: flex;
          align-items: center;

          .menu-toggle__text {
            margin-top: -4px;
            margin-right: 5px;
          }
        }
      }
    }
  }

  .view-wrapper {
    position: relative;
    display: flex;
    padding-top: 100px;
    background-color: $martinique;
    color: white;
    min-height: calc(100vh - 100px);

    &.menu-open {
      overflow: hidden;
    }
  }

  footer {
    display: flex;
    flex-direction: column;
    background-color: $martinique;
    align-items: center;
    justify-content: center;
    text-align: center;
    padding-top: 50px;
    padding-bottom: 50px;
    color: white;

    .footer-socials {
      padding: 20px 0;

      a {
        color: white;
        transition: color 0.25s ease;

        &:hover {
          color: $rose;
        }
      }
    }
  }
}
</style>
