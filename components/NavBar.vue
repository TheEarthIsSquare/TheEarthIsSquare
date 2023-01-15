<template>
  <nav>
    <NuxtLink :to="{ name: 'home' }" class="nav__icon">
      <Icon name="teis" size="4rem"/>
    </NuxtLink>

    <div class="nav__items">
      <NuxtLink :to="{ name: 'home' }" class="nav__item">
        Home
      </NuxtLink>

      <NuxtLink :to="{ name: 'course' }" class="nav__item">
        Course
      </NuxtLink>
    </div>

    <NuxtLink to="apply">
      <CoreButton :style="{ height: '100%', width: '10vw' }" size="L">
        Get Started
      </CoreButton>
    </NuxtLink>
  </nav>
</template>

<script lang="ts" setup>
import CoreButton from "./CoreButton.vue";</script>

<style lang="scss" scoped>
nav {
  font-size: var(--FontSize-L);
  font-weight: var(--FontWeight-Bold);
  position: absolute;
  z-index: 100;
  top: 0;
  right: 0;
  left: 0;
  display: flex;
  height: 11.6rem;
  padding: 0.6rem 0.6rem;
  border-radius: var(--BorderRadius-L);
  background-color: var(--Color-Black);
  gap: 0.6rem;

  .nav__icon {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 12rem;
    height: 100%;
    border-radius: var(--BorderRadius-L);
    background-color: var(--Color-White);
  }

  .nav__items {
    display: flex;
    align-items: center;
    flex: 1;
    justify-content: center;
    border-radius: var(--BorderRadius-L);
    background-color: var(--Color-White);
    gap: 2rem;

    .nav__item {
      transition: all 0.25s ease;
      text-transform: uppercase;

      &:hover {
        background: var(--Gradient-PinkPurple);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
      }

      &.router-link-exact-active {
        background: var(--Gradient-PinkPurple);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
      }
    }
  }
}
</style>