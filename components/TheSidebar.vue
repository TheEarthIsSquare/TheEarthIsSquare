<template>
  <div :class="{ '--open': isOpen }" class="sidebar__wrapper">
    <div class="sidebar">
      <nav class="sidebar__navigation">
        <div class="sidebar__navigation-header">
          The Earth<br />Is Square
        </div>

        <ul class="sidebar__navigation-items">
          <li class="sidebar__navigation-item">
            <router-link :to="{ name: 'index' }">
              Home
            </router-link>
          </li>

          <li class="sidebar__navigation-item --construction">
            <a>Academy</a>
          </li>

          <li class="sidebar__navigation-item --construction">
            <a>Our Powers</a>
          </li>

          <li class="sidebar__navigation-item --construction">
            <a>Our Work</a>
          </li>

          <li class="sidebar__navigation-item --construction">
            <a>About</a>
          </li>

          <li class="sidebar__navigation-item">
            <router-link :to="{ name: 'contact' }">Contact Us</router-link>
          </li>
        </ul>

        <div class="sidebar__socials">
          <a href="https://instagram.com/_earthissquare" target="_blank">
            <Icon name="instagram" size="36px" />
          </a>
          <a href="https://twitter.com/_earthissquare" target="_blank">
            <Icon name="twitter" size="36px" />
          </a>
          <a href="https://www.youtube.com/channel/UC_FBMBKup_b3xk_NfeKlalQ" target="_blank">
            <Icon name="youtube" size="36px" />
          </a>
          <a href="https://discord.com/invite/X23epKN" target="_blank">
            <Icon name="discord" size="36px" />
          </a>
          <a href="https://www.linkedin.com/company/the-earth-is-square" target="_blank">
            <Icon name="linkedIn" size="36px" />
          </a>
        </div>
      </nav>

      <div class="sidebar__overflow" @click="toggleSidebar()">
        <div class="sidebar__overflow-icon">
          <Icon name="teis" size="24px" />
        </div>

        <div class="sidebar__overflow-opener">
          <div class="sidebar__overflow-arrow">
            <Icon :name="isOpen ? 'leftArrowAlt' : 'rightArrowAlt'" size="24px" />
          </div>
          <div class="sidebar__overflow-arrow-back" />
        </div>

        <div class="sidebar__overflow-tagline">
          think outside the square.
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
const emit = defineEmits(["toggle-sidebar"]);
defineProps({
  isOpen: Boolean
});

const toggleSidebar = () => {
  emit("toggle-sidebar");
};
</script>

<style lang="scss" scoped>
.sidebar__wrapper {
  position: absolute;
  top: 0;
  bottom: 0;
  left: -300px;
  display: flex;
  width: 75px;
  transition: left 0.25s ease;

  .sidebar {
    display: flex;
    flex: 1;
    background-color: white;

    .sidebar__navigation {
      display: flex;
      flex-direction: column;
      width: 300px;

      padding: 50px 20px;
      transition: all 0.25s ease;
      opacity: 1;

      .sidebar__navigation-header {
        font-family: 'Passion One', sans-serif;
        font-size: 34px;
        font-weight: 900;
        line-height: 72%;
        margin-left: 20px;
        transform: rotate(-5deg);
        transform-origin: left top;
        text-transform: uppercase;
      }

      .sidebar__navigation-items {
        margin: 20px 0 10px 0;
        padding-left: 0;
        list-style: none;

        .sidebar__navigation-item {
          font-size: 24px;
          font-weight: bold;
          padding: 5px 0;
          transition: all 0.25s ease;
          transform-origin: left;

          &:hover {
            transform: scale(1.2, 1.2)
          }

          &.--construction {
            pointer-events: none;
            opacity: 0.2;
          }

          a {
            display: flex;

            &.router-link-exact-active {
              color: #D909DD;

              &:before {
                width: 2px;
                height: 100%;
                content: "";
                background-color: #D909DD;
              }
            }
          }
        }
      }

      .sidebar__socials {
        display: grid;
        grid-auto-flow: column;
        grid-auto-columns: 36px;
        grid-gap: 6px;

        a {
          transition: fill 0.25s ease;

          &:hover {
            fill: #D909DD;
          }
        }
      }
    }

    .sidebar__overflow {
      position: relative;
      display: flex;
      align-items: center;
      flex: 1;
      flex-direction: column;
      width: 75px;
      cursor: pointer;

      .sidebar__overflow-icon {
        margin-top: 20px;
      }

      .sidebar__overflow-opener {
        position: absolute;
        top: 10%;
        right: -13px;
        display: flex;
        align-items: center;
        justify-content: center;

        .sidebar__overflow-arrow {
          position: absolute;
          z-index: 100;
        }

        .sidebar__overflow-arrow-back {
          width: 26px;
          height: 26px;
          transform: rotate(45deg);
          background-color: white;
        }
      }

      .sidebar__overflow-tagline {
        font-size: 18px;
        font-weight: bold;
        position: absolute;
        bottom: 10%;
        width: 250px;
        transform: rotate(-90deg);
      }
    }
  }

  &.--open {
    left: 0;
  }
}
</style>