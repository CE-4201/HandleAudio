import { StatusBar } from "expo-status-bar";
import { StyleSheet, Text, View } from "react-native";

export default function Transcribed() {
  return (
    <View style={styles.container}>
      <Text style={styles.text}>This is the Transcribed text</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  text: {
    fontWeight: "600",
    fontSize: 20,
  },
  container: {
    flex: 1,
    backgroundColor: "#fff",
    alignItems: "center",
    justifyContent: "center",
  },
});
