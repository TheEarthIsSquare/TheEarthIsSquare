<template>
  <HomePanel
      :colSpan="isDesktop ? '8' : '12'" :rowSpan="isDesktop ? '5' : '6'" isExternalLink midGap="1rem"
      to="https://revolverlane.com"
  >
    <template v-slot:bg>
      <Duotone color="Pink">
        <img alt="Revolver Lane" src="~/assets/img/revolver-lane_2_2bit.avif"/>
      </Duotone>
    </template>

    <Heading type="h4">Welcome To Our Home</Heading>
    <div class="location__logo">
      <img alt="Revolver Lane Logo" src="~/assets/img/revolver-lane_logo.png"/>
    </div>
  </HomePanel>
</template>

<script lang="ts" setup>
import { useScreen } from "~/hooks/useScreen";

const { isDesktop } = useScreen();
</script>

<style lang="scss" scoped>
@import 'assets/style/variables.scss';

.location__logo {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 120%;
  margin-right: -10%;
  margin-left: -10%;
  padding: 2rem 0;
  transition: all 0.25s ease;
  border: 0.3rem solid var(--Color-Black);
  background-color: var(--Color-White);
  box-shadow: var(--Shadow-L);
  z-index: 10;

  img {
    width: 20%;
    height: auto;
    margin-top: -0.5rem;

    @media screen and (max-width: $BreakPoint-Tablet) {
      width: 60%;
    }
  }
}
</style>