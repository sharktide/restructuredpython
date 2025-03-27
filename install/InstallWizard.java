import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class InstallWizard {
    public static void main(String[] args) {
        // Create the main frame
        JFrame frame = new JFrame("Install Wizard");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(600, 400);
        frame.setLayout(new CardLayout()); // Use CardLayout for wizard-like behavior

        // Panels for wizard steps
        JPanel welcomePanel = new JPanel();
        JLabel welcomeLabel = new JLabel("Welcome to the reStructuredPython Install Wizard!");
        welcomePanel.setLayout(new BorderLayout());
        welcomePanel.add(welcomeLabel, BorderLayout.NORTH);

        JPanel installationPanel = new JPanel();
        JCheckBox vscodeCheckbox = new JCheckBox("Install Visual Studio Code Extension?");
        JButton backButton = new JButton("Back");
        JButton nextButton = new JButton("Install");
        installationPanel.add(vscodeCheckbox);
        installationPanel.add(backButton);
        installationPanel.add(nextButton);

        JPanel installingPanel = new JPanel();
        installingPanel.setLayout(new BorderLayout());
        JTextArea logArea = new JTextArea();
        logArea.setEditable(false);
        JScrollPane logScrollPane = new JScrollPane(logArea);
        JLabel installingLabel = new JLabel("Installing...");
        installingPanel.add(installingLabel, BorderLayout.NORTH);
        installingPanel.add(logScrollPane, BorderLayout.CENTER);

        JPanel finalPanel = new JPanel();
        JLabel finalLabel = new JLabel("Installation Complete!");
        finalPanel.add(finalLabel);
        JButton finishButton = new JButton("Finish");
        finalPanel.add(finishButton);

        // Add panels to frame
        frame.add(welcomePanel, "Welcome");
        frame.add(installationPanel, "Install Options");
        frame.add(installingPanel, "Installing");
        frame.add(finalPanel, "Final Step");

        // Create a CardLayout controller
        CardLayout cardLayout = (CardLayout) frame.getContentPane().getLayout();

        // Next button action (from welcome to installation options)
        JButton welcomeNextButton = new JButton("Next");
        welcomePanel.add(welcomeNextButton, BorderLayout.SOUTH);
        welcomeNextButton.addActionListener(e -> cardLayout.show(frame.getContentPane(), "Install Options"));

        // Back button action (from installation options to welcome)
        backButton.addActionListener(e -> cardLayout.show(frame.getContentPane(), "Welcome"));

        // Install button action (from installation options to installing)
        nextButton.addActionListener(e -> {
            cardLayout.show(frame.getContentPane(), "Installing");

            new Thread(() -> {
                try {
                    // Install the 'restructuredpython' package and show logs
                    ProcessBuilder pipBuilder = new ProcessBuilder("pip", "install", "--upgrade", "restructuredpython");
                    Process pipProcess = pipBuilder.start();
                    BufferedReader pipReader = new BufferedReader(new InputStreamReader(pipProcess.getInputStream()));

                    String line;
                    while ((line = pipReader.readLine()) != null) {
                        logArea.append(line + "\n");
                    }
                    pipProcess.waitFor();

                    logArea.append("Python package 'restructuredpython' installed successfully!\n");

                    // If checkbox is selected, install VS Code extension
                    if (vscodeCheckbox.isSelected()) {
                        String os = System.getProperty("os.name").toLowerCase();
                        ProcessBuilder vscodeBuilderWin = new ProcessBuilder(
                            "cmd.exe",
                            "/c",
                            "code --install-extension RihaanMeher.restructuredpython --force"
                        );
                        ProcessBuilder vscodeBuilderUnix = new ProcessBuilder(
                            "bash",
                            "-c",
                            "code --install-extension RihaanMeher.restructuredpython --force"
                        );

                        Process vscodeProcess = null;
                        if (os.contains("win")) {
                            logArea.append("Running on Windows\n");
                            vscodeProcess = vscodeBuilderWin.start();
                        } else if (os.contains("mac") || os.contains("nix") || os.contains("nux") || os.contains("aix")) {
                            logArea.append("Running on macOS/Linux\n");
                            vscodeProcess = vscodeBuilderUnix.start();
                        } else {
                            throw new Exception("Unknown OS");
                        }

                        BufferedReader vscodeReader = new BufferedReader(new InputStreamReader(vscodeProcess.getInputStream()));
                        while ((line = vscodeReader.readLine()) != null) {
                            logArea.append(line + "\n");
                        }
                        vscodeProcess.waitFor();

                        logArea.append("VS Code extension 'RihaanMeher.restructuredpython' installed successfully!\n");
                    }

                    // Move to final step
                    SwingUtilities.invokeLater(() -> cardLayout.show(frame.getContentPane(), "Final Step"));
                } catch (Exception ex) {
                    SwingUtilities.invokeLater(() -> logArea.append("Error during installation: " + ex.getMessage() + "\n"));
                }
            }).start();
        });

        // Finish button action (exit the wizard)
        finishButton.addActionListener(e -> System.exit(0));

        // Show the frame
        frame.setVisible(true);
    }
}
