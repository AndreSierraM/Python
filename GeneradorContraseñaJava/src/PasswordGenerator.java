import java.awt.BorderLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.Random;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JTextArea;

public class PasswordGenerator {
    private JFrame frame;
    private JTextArea passwordTextArea;
    
    public PasswordGenerator() {
        createUI();
    }
    
    private void createUI() {
        frame = new JFrame("Password Generator");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        
        JPanel panel = new JPanel();
        passwordTextArea = new JTextArea(1, 20);
        passwordTextArea.setEditable(false);
        panel.add(passwordTextArea);
        
        JButton generateButton = new JButton("Generate");
        generateButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                generatePassword();
            }
        });
        panel.add(generateButton);
        
        frame.getContentPane().add(panel, BorderLayout.CENTER);
        frame.pack();
        frame.setVisible(true);
    }
    
    private void generatePassword() {
        String characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+";
        int length = 12;
        Random random = new Random();
        StringBuilder password = new StringBuilder();
        for (int i = 0; i < length; i++) {
            int index = random.nextInt(characters.length());
            password.append(characters.charAt(index));
        }
        passwordTextArea.setText(password.toString());
    }
    
    public static void main(String[] args) {
        PasswordGenerator passwordGenerator = new PasswordGenerator();
    }
}
