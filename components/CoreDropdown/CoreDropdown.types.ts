import type { IconName } from "@/components/Icon/IconRegistry";

export interface DropdownOption {
    value: string;
    label: string;
    leftImage?: string;
    leftIcon?: IconName;
}