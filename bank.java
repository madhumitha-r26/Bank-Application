import java.util.Scanner;

public class bank {
    int acc_no;
    String name, acc_type;
    float bal;
    Scanner ob = new Scanner(System.in);

    void getValues() {
        System.out.print("Enter account number:");
        acc_no = ob.nextInt();
        System.out.print("Enter name:");
        name = ob.nextLine();
        System.out.print("Enter account type:");
        acc_type = ob.nextLine();
        System.out.print("Enter balance:");
        bal = ob.nextFloat();
    }

    void deposit() {
        int amount;
        System.out.println("\t"+"DEPOSIT PROCESS"+"\t");
        System.out.print("Amount to be deposited:");
        amount = ob.nextInt();
        bal += amount;
        System.out.print("Current balance: " + bal);
       
    }

    void withdraw() {
        int amount;
        System.out.println("\t"+"WITHDRAW PROCESS"+"\t");
        System.out.print("Amount to be withdrawn:");
        amount = ob.nextInt();
        if(bal>0)
        {
            bal -= amount;
            System.out.print("Current balance: " + bal);
        }
        else
        {
            System.out.print("No balance: ");
        }
    }

    void display() {
        System.out.println("\t"+"DETAILS"+"\t");
        System.out.print("Account number: " + acc_no);
        System.out.print("Name: " + name);
        System.out.print("Account type: " + acc_type);
        System.out.print("Current balance: " + bal);
    }

    public static void main(String args[]) {
    
        bank b = new bank();
        b.getValues();
        b.deposit();
        b.withdraw();
        b.display();
            
        } 
       
    }
