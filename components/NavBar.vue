<template>
  <nav>
    <RouterLink :to="{ name: 'home' }" class="nav__icon">
      <Icon name="teis" size="4rem" />
    </RouterLink>

    <div class="nav__items">
      <RouterLink :to="{ name: 'home' }" class="nav__item">
        Home
      </RouterLink>

      <!--      <RouterLink :to="{ name: 'info' }" class="nav__item">-->
      <!--        Info-->
      <!--      </RouterLink>-->

      <RouterLink :to="{ name: 'course' }" class="nav__item">
        Course
      </RouterLink>
    </div>

    <router-link to="apply">
      <CoreButton height="100%" width="10vw">
        Get Started
      </CoreButton>
    </router-link>
  </nav>
</template>

<script lang="ts" setup>
import CoreButton from "./CoreButton.vue";</script>

<style lang="scss" scoped>
nav {
  font-size: 24.88px;
  font-weight: bold;
  position: absolute;
  z-index: 100;
  top: 0;
  right: 0;
  left: 0;
  display: flex;
  height: 11.6rem;
  padding: 0.6rem 0.6rem;
  border-radius: 3rem;
  background-color: var(--black);
  gap: 0.6rem;

  .nav__icon {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 12rem;
    height: 100%;
    border-radius: 3rem;
    background-color: var(--white);
  }

  .nav__items {
    display: flex;
    align-items: center;
    flex: 1;
    justify-content: center;
    border-radius: 3rem;
    background-color: var(--white);
    gap: 2rem;

    .nav__item {
      transition: all 0.25s ease;
      text-transform: uppercase;

      &:hover {
        color: var(--pink);
      }

      &.router-link-exact-active {
        color: var(--pink);
      }
    }
  }
}
</style>